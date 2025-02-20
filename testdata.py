import sqlite3

con = sqlite3.connect("mentalhealth.db")
cur = con.cursor()
cur.execute("""
    INSERT INTO "day" ("date", "mood", "sleep", "note", "focus") VALUES
    ('2025-02-01 08:00:00', 7, 6.5, 'Felt refreshed in the morning.', 3),
    ('2025-02-02 08:30:00', 5, 5.0, 'Tossed and turned all night.', 2),
    ('2025-02-03 07:45:00', 8, 7.5, 'Had a great start to the day.', 4),
    ('2025-02-04 09:00:00', 6, 6.0, 'A bit groggy but manageable.', 3),
    ('2025-02-05 08:15:00', 4, 4.5, 'Could not concentrate much.', 1),
    ('2025-02-06 07:30:00', 9, 8.0, 'Very productive day.', 5),
    ('2025-02-07 09:10:00', 3, 5.5, 'Woke up too late.', 2),
    ('2025-02-08 08:45:00', 6, 7.0, 'Normal day, nothing special.', 3),
    ('2025-02-09 07:50:00', 7, 6.8, 'Mild headache in the afternoon.', 3),
    ('2025-02-10 09:30:00', 5, 5.0, 'Worked late last night.', 2),
    ('2025-02-11 08:20:00', 8, 7.5, 'Good focus today.', 4),
    ('2025-02-12 07:40:00', 6, 6.5, 'Feeling okay but a little tired.', 3),
    ('2025-02-13 09:15:00', 4, 5.2, 'Did not sleep well.', 2),
    ('2025-02-14 08:00:00', 7, 6.9, 'Feeling content.', 3),
    ('2025-02-15 07:35:00', 9, 8.1, 'Best sleep in weeks!', 5),
    ('2025-02-16 09:25:00', 5, 5.4, 'Slightly stressed.', 2),
    ('2025-02-17 08:10:00', 6, 6.6, 'Decent day overall.', 3),
    ('2025-02-18 07:55:00', 8, 7.8, 'Feeling productive and positive.', 4),
    ('2025-02-19 09:05:00', 7, 6.7, 'No major complaints.', 3),
    ('2025-02-20 08:30:00', 5, 5.1, 'Need to improve my sleep schedule.', 2);
    """)
con.commit()
con.close()
