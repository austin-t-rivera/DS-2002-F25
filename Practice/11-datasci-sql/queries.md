# SQL Queries

Note about NULL: Null represents the absence of any value in a SQL table.
This should be understood as different from an "empty" value of `''` or `""`.

## SELECT

```
SELECT * FROM tracking;
SELECT * FROM tracking LIMIT 5;
SELECT * FROM tracking WHERE id = '009d9a0f-27b9-4ba3-bdbd-36bc7270e5ac';
SELECT * FROM tracking WHERE telem_1 > 0.8 AND telem_2 < 0.03;
SELECT * FROM tracking ORDER BY created_on ASC;
SELECT id, project_id, telem_1, telem2 FROM tracking LIMIT 10;
SELECT COUNT(*) FROM tracking WHERE ....;
```

## INSERT

```
INSERT INTO tracking 
  (id, project_id, telem_1, telem_2, longitude, latitude, created_on) 
VALUES 
  ('b982b24e-58f6-4b64-b628-69fc5d21817d', 5, 0.4868, 0.9338, 17.0088511, 60.6830311, '2020-02-21T23:44:16Z');

INSERT INTO tracking 
  (id, project_id, created_on) 
VALUES 
  ('b982b24e-58f6-4b64-b628-69fc5d91817d', 5, '2020-02-21T23:44:16Z');
```

## UPDATE

```
UPDATE tracking
  SET project_id = 4
  WHERE id = 'b982b24e-58f6-4b64-b628-69fc5d21817d';
```

## DELETE

```
DELETE FROM tracking WHERE id = 'xxxx';
DELETE FROM tracking WHERE created_on = "YYYY-MM-DD HH:MM:SS";
DELETE FROM tracking;
DROP tracking;
```

## JOIN

```
SELECT tracking.id, tracking.telem_1,
  projects.project_name 
FROM tracking 
INNER JOIN projects ON 
  tracking.project_id = projects.project_id;
```