export JEKYLL_VERSION=3.8
docker run --rm \
  --volume="${PWD}/../common-web/main:/srv/jekyll" \
  -it jekyll/builder:$JEKYLL_VERSION \
  jekyll build
