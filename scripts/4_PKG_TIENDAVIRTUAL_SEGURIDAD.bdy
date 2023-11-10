create or replace noneditionablejose package body PKG_TIENDAVIRTUAL_SEGURIDAD_JOSE is
  -- prueba
PROCEDURE SP_MOSTRAR_MENSAJE AS
  BEGIN
    DBMS_OUTPUT.put_line('Mensaje de prueba poc 1.1');
  END;

end PKG_TIENDAVIRTUAL_SEGURIDAD_JOSE;
/