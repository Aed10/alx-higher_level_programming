-- displays the max temperature of each state (ordered by State name).
SELECT
    DISTINCT state,
    value
FROM
    temperatures
HAVING
    value = (
        SELECT
            Max(value)
        FROM
            temperatures
    )
ORDER BY
    state;