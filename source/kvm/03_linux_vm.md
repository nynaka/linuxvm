Linux VM
===

## Linux

### Debian Linux 12

1. OS インストール ISO ファイルの取得

    ```bash
    wget https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.5.0-amd64-netinst.iso \
        -O /tmp/debian-12.5.0-amd64-netinst.iso
    ```

2. `--os-variant` の設定の取得

    ```bash
    osinfo-query os | grep debian
    ```

3. ISO イメージの起動

    ```bash
    virt-install \
        --name debian12 \
        --hvm \
        --ram 2048 \
        --disk size=20 \
        --vcpus 2 \
        --os-variant debian12 \
        --graphics none \
        --network bridge=virbr1 \
        --console pty,target_type=serial \
        --extra-args 'console=ttyS0,115200n8 serial' \
        --location /tmp/debian-12.5.0-amd64-netinst.iso,kernel=install.amd/vmlinuz,initrd=install.amd/initrd.gz
    ```

    GUI 無しでインストールする場合は、インストーラのカーネルに console 関連の引数を追加する都合で、ISO イメージのファイルパスの他に、ISO イメージ内のインストーラのカーネルパスと initrd のパスを指定する必要があるようです。

4. ネットワークインストールする場合

    ```bash
    sudo virt-install \
        --name debian12 \
        --hvm \
        --ram 2048 \
        --disk size=20 \
        --vcpus 2 \
        --os-variant debian12 \
        --graphics none \
        --network bridge=virbr0 \
        --console pty,target_type=serial \
        --extra-args 'console=ttyS0,115200n8 serial' \
        --location 'http://ftp.debian.org/debian/dists/stable/main/installer-amd64/'
    ```


### Fedora Server 40

1. `--os-variant` の設定の取得

    ```bash
    osinfo-query os | grep fedora
    ```

2. ISO イメージの起動

    ```bash
    virt-install \
        --name fedora40 \
        --arch=x86_64 \
        --hvm \
        --ram 4096 \
        --disk size=20 \
        --vcpus 2 \
        --os-variant fedora39 \
        --network bridge=virbr1 \
        --graphics none \
        --console pty,target_type=serial \
        --extra-args 'console=ttyS0,115200n8 serial' \
        --location /tmp/Fedora-Server-netinst-x86_64-40-1.14.iso
    ```

    `--location` に ISO イメージ内のインストーラのカーネルパスと initrd のパスを指定する必要はないのですが、Fedora のテキストベースのインストールメニューに戸惑うと思います。

### Ubuntu Server 22.04

1. `--os-variant` の設定の取得

    ```bash
    osinfo-query os | grep ubuntu
    ```

2. ISO イメージの起動

    ```bash
    virt-install \
        --name ubuntu2404 \
        --arch=x86_64 \
        --hvm \
        --ram 4096 \
        --disk size=20 \
        --vcpus 2 \
        --os-variant ubuntu24.04 \
        --network bridge=virbr1 \
        --graphics none \
        --console pty,target_type=serial \
        --extra-args 'console=ttyS0,115200n8 serial' \
        --location /tmp/ubuntu-24.04-live-server-amd64.iso,kernel=casper/vmlinuz,initrd=casper/initrd
    ```

    GUI 無しでインストールする場合は、インストーラのカーネルに console 関連の引数を追加する都合で、ISO イメージのファイルパスの他に、ISO イメージ内のインストーラのカーネルパスと initrd のパスを指定する必要があるようです。

    * コマンドオプション

        - --name : 仮想マシンの名前
        - --arch : CPU のアーキテクチャ
        - --hvm
        - --vcpus : 仮想 CPU の数
        - --ram : メモリ量（MB）
        - --disk : ディスクサイズ（GB）
        - --os-variant
        - --network : network=default: ネットワークの設定
        - --graphics
        - --console : pty,target_type=serial
        - --extra-args : 'console=ttyS0,115200n8'
        - --location : ISO ファイルと、インストーラが格納されているパスに相当する情報


## BSD

```{warning}
CUI ではインストーラまでたどり着けない。。。  
当面、Virt Manager をインストールして、GUI でインストールしましょう。
```

### FreeBSD

1. インストーラをコンソールブートに固定する

    - iso ファイルのコピーを作成

        ```bash
        sudo mount -o loop /tmp/FreeBSD-14.1-RELEASE-amd64-bootonly.iso /mnt/
        mkdir /tmp/freebsd-iso
        sudo cp -r /mnt/* /tmp/freebsd-iso
        sudo cp -r /mnt/.disk /tmp/freebsd-iso
        ```

    - /tmp/freebsd-iso/boot/loader.conf に下記の設定を追加

        ```text
        echo 'console="comconsole"' | sudo tee /tmp/freebsd-iso/boot/loader.conf
        ```

    - iso ファイルの作成

        ```bash
        sudo apt install genisoimage

        cd /tmp/freebsd-iso
        sudo mkisofs \
            -o /tmp/FreeBSD-14.1-RELEASE-amd64-bootonly-custom.iso \
            -b boot/cdboot \
            -no-emul-boot \
            -r -J -c boot/boot.catalog \
            -boot-load-size 4 \
            -boot-info-table .
        ```

2. `--os-variant` の設定の取得

    ```bash
    osinfo-query os | grep freebsd
    ```

3. ISO イメージの起動

    ```bash
    virt-install \
        --name freebsd14.1 \
        --arch=x86_64 \
        --hvm \
        --ram 4096 \
        --disk size=20 \
        --vcpus 2 \
        --os-variant freebsd13.0 \
        --network bridge=virbr1 \
        --nographics \
        --serial pty -v \
        --cdrom /tmp/FreeBSD-14.1-RELEASE-amd64-bootonly-custom.iso
    ```

### NetBSD

1. `--os-variant` の設定の取得

    ```bash
    osinfo-query os | grep netbsd
    ```

2. ISO イメージの起動

    ```bash
    virt-install \
        --name netbsd10 \
        --arch=x86_64 \
        --hvm \
        --ram 4096 \
        --disk size=20 \
        --vcpus 2 \
        --os-variant netbsd9.0 \
        --network bridge=virbr1 \
        --video=vga \
        --graphics none \
        --console pty,target_type=serial \
        --cdrom /tmp/NetBSD-10.0-amd64.iso
    ```

## Windows

Windows は、最初から GUI インストールを前提とした方が確実です。  
Windows Server であれば、いろいろやればコンソールインストールできるかも？
