import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE_URL = "https://nexabot.id"


def load_api_key() -> str:
    key = os.environ.get("NEXABOT_API_KEY", "").strip()
    env_file = Path(__file__).resolve().parents[1] / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("NEXABOT_API_KEY="):
                key = key or line.split("=", 1)[1].strip().strip("\"'")
                break
    if not key or any(token in key.lower() for token in ("letak", "gantikan", "your_key", "xxxxxxxx")):
        raise RuntimeError("Set a real NEXABOT_API_KEY in the project .env or environment")
    return key


def api_request(method: str, path: str, body: dict | None = None) -> tuple[int, bytes]:
    key = load_api_key()
    headers = {"x-api-key": key, "User-Agent": "NexabotClient/1.0"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(BASE_URL + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: nexabot_client.py <credit|modes|submit|status|wait_and_download> ...")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "credit":
        code, raw = api_request("GET", "/api/v1/api/credit")
        print(code, raw.decode("utf-8", "replace"))
    elif cmd == "modes":
        code, raw = api_request("GET", "/api/v1/modes")
        print(code, raw.decode("utf-8", "replace")[:4000])
    elif cmd == "submit":
        if len(sys.argv) < 3:
            raise ValueError("submit requires a JSON payload")
        payload = json.loads(sys.argv[2])
        code, raw = api_request("POST", "/api/v1/api", payload)
        print(code, raw.decode("utf-8", "replace"))
    elif cmd == "status":
        if len(sys.argv) < 3:
            raise ValueError("status requires a job ID")
        job_id = sys.argv[2]
        code, raw = api_request("GET", f"/api/v1/jobs/{job_id}")
        print(code, raw.decode("utf-8", "replace"))
    elif cmd == "wait_and_download":
        if len(sys.argv) < 4:
            raise ValueError("wait_and_download requires a job ID and output path")
        job_id = sys.argv[2]
        out_path = Path(sys.argv[3])
        out_path.parent.mkdir(parents=True, exist_ok=True)
        for _ in range(180):
            code, raw = api_request("GET", f"/api/v1/jobs/{job_id}")
            data = json.loads(raw.decode("utf-8", "replace"))
            job = data.get("job", {})
            st = job.get("status")
            print(f"[{job_id}] status={st} progress={job.get('progress')} error={job.get('error')}", flush=True)
            if st == "done":
                dl_code, dl_bytes = api_request("GET", f"/api/v1/jobs/{job_id}/download")
                if dl_code != 200:
                    raise RuntimeError(f"Download failed HTTP {dl_code}: {dl_bytes[:300]!r}")
                out_path.write_bytes(dl_bytes)
                print(f"[{job_id}] saved {out_path} ({len(dl_bytes)} bytes)", flush=True)
                return
            if st == "failed":
                raise RuntimeError(f"Job {job_id} failed: {data}")
            time.sleep(5)
        raise TimeoutError(f"Timed out waiting for job {job_id}")
    else:
        raise ValueError(f"Unknown command: {cmd}")

    if code >= 400:
        sys.exit(1)


if __name__ == "__main__":
    main()
