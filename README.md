# GitLab Runner CI/CD

GitLab Runner를 컨테이너로 실행한 예시

```
Host System
├── Docker Daemon
    ├── GitLab Runner Container
    └── CI Job Container (직접 호스트의 Docker daemon 사용)
```

## Build
- Push
- Docker 이미지 빌드
- Container Registry에 이미지 업로드

## Deploy
- 최신 Docker 이미지 가져오기
- GitLab Runner 서버에서 컨테이너 실행

## Test

```
http://{ip}:9999/hello
```
