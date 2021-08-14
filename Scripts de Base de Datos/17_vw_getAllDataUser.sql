USE GameManager;

DROP VIEW IF EXISTS vm_getAllDataUser;

CREATE VIEW vm_getAllDataUser AS 
    SELECT
        big_id,
        var_firstName,
        var_lastName,
        var_email,
        var_nickname,
        CONVERT(AES_DECRYPT(var_password,'salt') USING utf8)
    FROM
        User
    ;