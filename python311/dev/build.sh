#!/bin/bash
export TAG=public.ecr.aws/k5v1i0e6/linkageruntime
if [ "$(uname -m)" = "aarch64" ]
then 
    export TAG="$TAG:arm64"
else 
    export TAG="$TAG:amd64"
fi	
docker build . -t "$TAG"
docker push "$TAG"
#make multi arch docker manifest here:
#docker manifest rm public.ecr.aws/k5v1i0e6/linkageruntime:latest
#docker manifest create public.ecr.aws/k5v1i0e6/linkageruntime:latest public.ecr.aws/k5v1i0e6/linkageruntime:arm64 public.ecr.aws/k5v1i0e6/linkageruntime:amd64
#docker manifest create public.ecr.aws/k5v1i0e6/linkageruntime:latest public.ecr.aws/k5v1i0e6/linkageruntime:arm64 public.ecr.aws/k5v1i0e6/linkageruntime:amd64 --amend
#docker manifest push public.ecr.aws/k5v1i0e6/linkageruntime:latest
#docker manifest inspect public.ecr.aws/k5v1i0e6/linkageruntime:latest
