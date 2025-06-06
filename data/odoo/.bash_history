odoo -u web --stop-after-init
exit
odoo -u all --stop-after-init
docker compose restart
exit
odoo -d odoo -u all --stop-after-init
exit
rm -rf /var/lib/odoo/.local/share/Odoo/filestore/odoo/assets
exit
