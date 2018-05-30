docker-compose exec bee-db mysql -u root -peyoo1oheesebiochedae0ThaePhainey beedb -e "CREATE USER guest@localhost IDENTIFIED BY readonly;"
docker-compose exec bee-db mysql -u root -peyoo1oheesebiochedae0ThaePhainey beedb -e "GRANT SELECT ON *.* TO guest@localhost IDENTIFIED BY readonly;"
