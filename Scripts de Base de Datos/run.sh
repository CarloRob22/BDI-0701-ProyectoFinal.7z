#!/bin/bash

echo "---------------------------------------------------------------------------"
echo "Hola! Bienvenido al asistente de creacion para la base de datos"
echo "---------------------------------------------------------------------------"

echo ""
echo "inserta tu usuario para acceder a MySQL: "
read MY_DB_USER

echo ""
echo "inserta tu clave de acceso para MySQL: "
read MY_DB_PASS

mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 1_DDS.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 2_DMS.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 3_sp_auth.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 4_tg_matchJournal.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 5_sp_sessionJournal.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 6_sp_gameMatch.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 7_sp_updateStateGameMatch.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 8_sp_getHoldMatch.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 9_sp_updateGameMatch.sql

echo ""
echo "------------------------------------------------------------------------------"
echo "Base de datos creada con exito!"
echo "-------------------------------------------------------------------------------"

