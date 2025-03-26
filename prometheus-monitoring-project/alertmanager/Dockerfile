FROM prom/alertmanager

COPY alertmanager.yml /etc/alertmanager/alertmanager.yml

ENTRYPOINT [ "/bin/alertmanager", "--config.file=/etc/alertmanager/alertmanager.yml" ]
