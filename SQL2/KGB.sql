-- Скрипт КГБ
-- По имени и фамилии выдает информацию о перемещения (совершенных, будущих и текущих)
-- Имя жертвы можно задать в предпоследней строке скрипта, список всех доступных имен
-- можно посмотреть в таблице 'tickets' с помощью скрипта
-- SELECT DISTINCT passenger_name FROM tickets ORDER BY passenger_name
SELECT tic.passenger_name AS "Пассажир",
	tic.book_ref AS "Номер брони",
	to_char(bookings.book_date, 'DD.MM.YYYY HH24:MI') AS "Дата бронирования",
	t_f.amount AS "Сумма",
	fl.flight_id AS "Номер рейса",
	a_d.city::jsonb->>'ru' AS "Аэропорт отправления",
	a_d1.city::jsonb->>'ru' AS "Аэропорт прибытия",
	to_char(fl.scheduled_departure, 'DD.MM.YYYY HH24:MI') AS "Дата отправления",
	CASE WHEN fl.status = 'Arrived'	THEN 'Завершен'
		WHEN fl.status = 'Scheduled' THEN 'Запланирован'
		WHEN fl.status = 'On Time' THEN 'В процессе'
		ELSE 'Другое'
	END AS "Статус рейса"
FROM tickets tic
JOIN bookings ON tic.book_ref = bookings.book_ref
JOIN ticket_flights t_f ON tic.ticket_no = t_f.ticket_no
JOIN flights fl ON t_f.flight_id = fl.flight_id
JOIN airports_data a_d ON fl.departure_airport = a_d.airport_code
JOIN airports_data a_d1 ON fl.arrival_airport = a_d1.airport_code
WHERE tic.passenger_name = 'ALBINA ANDREEVA'
ORDER BY fl.scheduled_departure ASC