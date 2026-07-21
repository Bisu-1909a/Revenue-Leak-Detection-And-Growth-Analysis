## Table 1 — Customers
## Why does this table exist?
Every order belongs to a customer.

Without customers...

There are no sales.

## Columns
Column	                  Data Type	                     Why?

customer_id	              INTEGER	           Unique customer identifier
customer_name	            TEXT	                 Customer name
segment	                    TEXT	                Retail / Wholesale
region	                    TEXT	                Business region
signup_date	                DATE	              Customer joined date

## Primary Key
customer_id


## Business Questions This Table Answers
-> Which region has the most customers?
-> Which customer segment generates more revenue?
-> How many new customers joined?


## Table 2 — Products

## Why?
The company sells products.

We need to know: 
-> selling price
-> cost
-> category


## Columns
Column	            Data Type	                Why?
product_id	            INTEGER	            Unique product
product_name	        TEXT	             Product name
category	            TEXT	          Electronics, Furniture...
brand	                TEXT	                Brand
cost_price	            REAL	            Business cost
list_price	            REAL	        Selling price before discount


## Primary Key
product_id

## Business Questions
-> Which category is most profitable?
-> Which products have low margins?



## Table 3 — Orders
## Why?
Every purchase becomes one order.

## Columns
Column	               Data Type	            Why?
order_id	            INTEGER	            Unique order
customer_id	            INTEGER	            Who placed the order
order_date	            DATE	            Purchase date
status	                TEXT	            Completed / Cancelled / Returned


## Primary Key
order_id


## Foreign Key
customer_id

## References
Customers


## Business Questions
-> Total orders
-> Monthly sales
-> Cancellation rate



## Table 4 — Order Items

Revenue

Profit

Discount

Quantity

Margin

Everything.

## Columns
Column	               Data Type	            Why?
order_item_id	        INTEGER	            Unique row
order_id	            INTEGER	            Related order
product_id	            INTEGER	            Product purchased
quantity	            INTEGER	            Units sold
unit_price	            REAL	            Selling price
discount_percent	    REAL	            Discount given


## Foreign Keys
order_id
product_id


## Business Questions
Revenue
Profit
Discount impact
Margin
Best-selling products




## Table 5 — Delivery
## Why?

Management thinks

Late deliveries
↓
Returns
↓
Revenue Leak

So we need delivery data.

## Columns
Column	           Data Type	        Why?
delivery_id	        INTEGER	        Unique delivery
order_id	        INTEGER	        Related order
dispatch_date	    DATE	        Sent date
delivery_date	    DATE	        Delivered date
courier	            TEXT	        Courier company
delivery_status	    TEXT	        Delivered / Delayed


## Business Questions
Average delivery delay
Late deliveries
Delay vs returns

## Complete Database

Customers
│
├── customer_id (PK)
│
└──────────────┐
               │
Orders         │
│              │
├── order_id (PK)
├── customer_id (FK)
│
└──────────────┐
               │
Order_Items    │
│              │
├── order_item_id (PK)
├── order_id (FK)
├── product_id (FK)
│
└──────────────┐
               │
Products       │
├── product_id (PK)

Orders
│
└──────────────► Delivery
                 ├── delivery_id (PK)
                 ├── order_id (FK)

