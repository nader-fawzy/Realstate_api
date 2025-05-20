# RealState API 
# 📄 Property Type Database Table Structure
This document outlines the structure of the **Property Classification** portion of the database, consisting of two related tables:

- `Property_Category`
- `Property_Type`
## 🏘️ Property Database Chart
![Database Schema](image/PropertyType.png)
---
### 📂 Property_Category Table

| Column        | Type    | Description                        |
|---------------|---------|------------------------------------|
| `id`          | int     | Primary key, auto-incremented.     |
| `category_en` | string  | Category name in English.          |
| `category_ar` | string  | Category name in Arabic.           |

---

### 🏷️ Property_Type Table

| Column     | Type    | Description                                                               |
|------------|---------|---------------------------------------------------------------------------|
| `id`       | int     | Primary key, auto-incremented.                                            |
| `type_en`  | string  | Property type name in English.                                            |
| `type_ar`  | string  | Property type name in Arabic.                                             |
| `category_id` | int  | Foreign key referencing `Property_Category.id`, links type to a category. |

# 📄 Location Database Table Structure
---
This project includes a structured database of **Countries**, **Cities**, and **Areas**, designed with clarity and integrity using foreign key relationships. Below is a detailed explanation of each table and its columns.

---
## Database Chart
![Database Schema](image/LocationDB.png)
---

## 🌍 Country Table

| Column Name   | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `id`          | Unique identifier for each country (Primary Key).                           |
| `country_en`  | Country name written in English.                                             |
| `country_ar`  | Country name written in Arabic.                                              |
| `status`      | Indicates whether the country is active (`1`) or inactive (`0`). Used instead of deletion. |

---

## 🏙️ City Table

| Column Name   | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `id`          | Unique identifier for each city (Primary Key).                              |
| `city_en`     | City name written in English.                                               |
| `city_ar`     | City name written in Arabic.                                                |
| `country_id`  | Foreign key referencing the `Country` table (`Many-to-One` relationship).   |
| `status`      | Indicates whether the city is active (`1`) or inactive (`0`).              |

---

## 📍 Area Table

| Column Name   | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `id`          | Unique identifier for each area (Primary Key).                              |
| `area_en`     | Area name written in English.                                               |
| `area_ar`     | Area name written in Arabic.                                                |
| `city_id`     | Foreign key referencing the `City` table (`Many-to-One` relationship).      |
| `status`      | Indicates whether the area is active (`1`) or inactive (`0`).              |

---

# 💱 Currency Converter Integration
This Django project include integrates with a **currency exchange API** to fetch real-time exchange rates, store them in a database, and reduce repetitive API calls by populating a local table once per day.

---

## 🚀 Features

- Fetches exchange rates from a reliable currency API (e.g., [ExchangeRate-API](https://www.exchangerate-api.com/))
- Stores exchange rates in a database table `CurrencyConverter`
- Supports converting from a **base currency** (e.g., `EGP`) to over 100+ currencies
- Avoids unnecessary API calls by updating rates only **once per day**
- Custom Django management command: `update_currencies`

---

## 📦 `CurrencyConverter` Table Structure

| Field            | Type      | Description                                       |
|------------------|-----------|---------------------------------------------------|
| `base_currency`  | CharField | The currency from which conversion starts (e.g., `EGP`) |
| `target_currency`| CharField | The destination currency (e.g., `USD`, `EUR`)    |
| `rate`           | Float     | The conversion rate stored for that day          |

---

# 🏡 Property Currency Conversion

### 🔁 `/get_all_property/` Endpoint

This endpoint returns all properties with their prices **converted into a selected currency** .

- Conversion is dynamic based on stored exchange rates.
- Default target currency can be customized from the frontend or request params (TBD).

### 🔧 Currency Conversion Logic

Utility function:

```python
def property_convert_currancy(property_price, property_c, target_c):
    currancy_rate = CurrencyConverter.objects.values('target_currency', 'rate')
    rate_dict = {item['target_currency']: item['rate'] for item in currancy_rate}
    rate_from = rate_dict[property_c]
    rate_to = rate_dict[target_c]
    property_price = Decimal(property_price)
    converted_amount = (property_price / rate_from) * rate_to
    return round(converted_amount, 2)