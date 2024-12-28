# MySQL Database Tables

---

## **Attendance Table**

| **Field**   | **Type**         | **Null** | **Key** | **Default** | **Extra** |
|-------------|------------------|----------|---------|-------------|-----------|
| name        | varchar(200)     | YES      |         | NULL        |           |
| date_time   | datetime         | YES      |         | NULL        |           |

---

## **Detected Faces Table**

| **Field**   | **Type**         | **Null** | **Key** | **Default** | **Extra** |
|-------------|------------------|----------|---------|-------------|-----------|
| name        | varchar(200)     | YES      |         | NULL        |           |
| image_path  | varchar(200)     | YES      |         | NULL        |           |

---

## **Events Table**

| **Field**             | **Type**         | **Null** | **Key** | **Default** | **Extra** |
|-----------------------|------------------|----------|---------|-------------|-----------|
| GRNo                 | int              | YES      |         | NULL        |           |
| event_date           | date             | YES      |         | NULL        |           |
| event_description    | varchar(255)     | YES      |         | NULL        |           |

---

## **Files Table**

| **Field**   | **Type**         | **Null** | **Key** | **Default** | **Extra** |
|-------------|------------------|----------|---------|-------------|-----------|
| Name        | varchar(150)     | YES      |         | NULL        |           |
| filename    | varchar(180)     | YES      |         | NULL        |           |

---

## **Students Table**

| **Field**   | **Type**         | **Null** | **Key** | **Default** | **Extra** |
|-------------|------------------|----------|---------|-------------|-----------|
| GRNo        | int              | YES      |         | NULL        |           |
| Name        | varchar(200)     | YES      |         | NULL        |           |
| Class       | varchar(10)      | YES      |         | NULL        |           |

---

## **TipofDay Table**

| **Field**   | **Type** | **Null** | **Key** | **Default** | **Extra** |
|-------------|----------|----------|---------|-------------|-----------|
| tip_text    | text     | YES      |         | NULL        |           |

---

## **Users Table (for login)**

| **Field**   | **Type**        | **Null** | **Key** | **Default** | **Extra** |
|-------------|-----------------|----------|---------|-------------|-----------|
| GRNo        | int             | YES      |         | NULL        |           |
| username    | varchar(80)     | YES      |         | NULL        |           |
| password    | varchar(80)     | YES      |         | NULL        |           |
