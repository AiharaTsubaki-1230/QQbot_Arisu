docker run -d --restart=always --memory 1g --memory-swap 2g --name qsign -p 8080:8080 -e ANDROID_ID=87b9225f1cd87e77 xzhouqd/qsign:8.9.63
docker run -d --restart=always --name qsign -p 8000:8080 -e ANDROID_ID=87b9225f1cd87e77 -e COUNT=1 xzhouqd/qsign:8.9.63

docker run -d --restart=always --name qsign -p 8000:8080 -e BASE_PATH=/srv/qsign/qsign/txlib/8.9.73 xzhouqd/qsign:core-1.1.9



docker run -d --restart=always --name qsign -p 8000:8080 -e BASE_PATH=/srv/qsign/qsign/txlib/8.9.73 -v {host_abs_config.json_path}:/srv/qsign/qsign/txlib/{version}/config.json xzhouqd/qsign:core-{core-ver}