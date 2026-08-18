# demo-service

The smallest possible service, used to practice the company's git & CI/CD
flow. One Python file, stdlib only, tests included in the file.

```bash
python3 app.py                 # run it — serves on port 8000
python3 -m unittest app        # test it
curl localhost:8000/           # → {"service": ..., "version": ..., "git_sha": ...}
```

The `/` endpoint reports the service's version and the git commit it was
built from — that answer is the proof at every step of the pipeline below.

## How a change ships

```
you: branch → PR ──▶ verify.yml   tests on every PR          (staging runner)
         merge ────▶ build.yml    build image demo-service:git-<sha>,
                                  deploy to staging :8081, e2e-test it
you: tag v* ───────▶ release.yml  WAITS for human approval, then deploys
                                  the same already-tested image to prod :8082
```

Rules enforced by branch protection: no direct pushes to `main`, the
`verify` check must pass, branches must be up to date, squash merges only.

Rules enforced by design: the image is built **once** per merge — releases
never rebuild; production only changes when a human tags **and** approves.

## Files

| File | Role |
|---|---|
| `app.py` | the app + its tests |
| `Dockerfile` | recipe for the sealed package (`GIT_SHA` stamped at build) |
| `.github/workflows/verify.yml` | robot 1: test every PR |
| `.github/workflows/build.yml` | robot 2: build + deploy staging + e2e, on merge |
| `.github/workflows/release.yml` | robot 3: deploy prod, on tag + approval |

This repo is part of a teaching demo — the full step-by-step walkthrough
(including the servers' side of the story) lives in the company's
`TechStructResearch/demo/` folder.
