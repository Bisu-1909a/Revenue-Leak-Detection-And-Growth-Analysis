# Database Design

## Business Entities

### Customers
Stores customer information.

### Products
Stores product information.

### Orders
Stores order details placed by customers.

### Order Items
Stores product-level details for each order.

### Delivery
Stores delivery information for each order.

---

## Relationship
Customer → Orders

Orders → Order Items

Products → Order Items

Orders → Delivery
