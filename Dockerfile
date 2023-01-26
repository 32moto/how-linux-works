FROM ubuntu:latest

RUN apt-get update

ENV TZ Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

RUN apt-get install -y locales && \
    locale-gen ja_JP.UTF-8 && \
    echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

RUN apt-get install -y \
    strace \
    psmisc \
    man

RUN apt-get install -y \
    binutils \
    build-essential \
    golang \
    sysstat \
    python3-matplotlib \
    python3-pil \
    fonts-takao \
    fio \
    qemu-kvm \
    virt-manager \
    libvirt-clients \
    virtinst \
    jq \
    docker.io \
    containerd \
    libvirt-daemon-system

RUN adduser `id -un` libvirt && \
    adduser `id -un` libvirt-qemu && \
    adduser `id -un` kvm