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
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 10_fn_weighing.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 11_sp_addScore.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 12_sp_addMoveMatch.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 13_sp_getFirstMove.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 14_sp_getLastMove.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 15_sp_delMoveMatch.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 16_sp_restartGameMatch.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 17_vw_getAllDataUser.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 18_sp_deleteUser.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 19_sp_getUser.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 20_sp_insertUser.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 21_sp_updateDataUser.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 22_tg_scoreJournal.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 23_sp_getAllDataMatchHold.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 24_spcu_getUserScore.sql
mysql -t -v -u "$MY_DB_USER" -p"$MY_DB_PASS" < 28_sp_updateJsonMoves.sql

echo ""
echo "------------------------------------------------------------------------------"
echo "Base de datos creada con exito!"
echo "-------------------------------------------------------------------------------"

