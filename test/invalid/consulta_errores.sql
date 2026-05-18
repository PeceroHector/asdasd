DECLARE @mi_variable INT;

SELECT id, nombre, salario$ 
FROM empleados#temporales
WHERE activo = TRUE;

WITH Ventas AS (
    SELECT 
        vendedor_id, 
        total ~ descuento AS total_real 
    FROM ventas_diarias
)
SELECT * FROM Ventas;

GRANT SELECT ON ?tabla_desconocida TO usuario;



