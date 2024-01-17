create or replace noneditionable package body pdbadmin.PKG_TIENDAVIRTUAL_SEGURIDAD is
-- prueba 5
PROCEDURE SP_MOSTRAR_MENSAJE AS
  BEGIN
    DBMS_OUTPUT.put_line('Estamos en el Curso Oracle´en Multiverso TI');
  END;

end PKG_TIENDAVIRTUAL_SEGURIDAD;
/
