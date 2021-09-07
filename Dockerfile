FROM direvius/yandex-tank
ADD configs/tank.yaml /var/tank/tank.yaml
ADD ammo.txt /var/tank/ammo.txt
ENTRYPOINT yandex-tank -c /var/tank/tank.yaml