sudo apt update
sudo apt install prometheus
sudo apt install grafana
pip install flask


#한번 docker compose up하면 폴더생성됨.
sudo chmod 644 /home/$USER/monitoring/prometheus/json_exporter_config.json   
sudo chmod 644 /home/$USER/monitoring/prometheus/prometheus.yml               
sudo chmod 777 /home/$USER/monitoring/prometheus/data
sudo chmod 777 /home/$USER/monitoring/prometheus/logs
sudo chmod 777 /home/$USER/monitoring/grafana/data
sudo chmod 777 /home/$USER/monitoring/grafana/logs

권한 부여 후 
docker compose down
docker compose up
