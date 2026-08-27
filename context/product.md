# Product Context — Order Management

## Product

E-commerce application for a music store selling musical instruments.

MVP product categories:

- string instruments
- keyboard instruments
- wind instruments

## Target Users

Registered customers.

Admin users and administrative functionality are out of scope for the MVP.

Future consideration:
A separate admin application may be introduced for managing products,
orders and users.

## Problem

The business currently operates a physical music store and wants to enable
customers to purchase musical instruments online.

## Business Goal

Enable the store to sell musical instruments online to registered customers
through a simple and reliable purchasing process.

## MVP Success

A registered customer can successfully purchase an available musical
instrument through the website using the test payment flow and receive an
order confirmation email.

## Scope

### Account

- User registration
- User login

### Product Discovery

- Product listing
- Product details

### Shopping

- Add product to cart
- Cart
- Checkout

### Order

- Shipping method selection
- Test payment
- Order confirmation
- Confirmation email

### Payment

Payment is simulated for the MVP.
No real payment provider integration is implemented.

### Shipping

Shipping method selection is supported.
No real courier/shipping provider integration is implemented.

### Email

A real confirmation email is sent after a successful order.

In the MVP/test environment, email delivery is restricted to whitelisted
email addresses.

## Out of Scope

- Real payment provider integration
- Real courier/shipping provider integration
- Formal performance/load/stress testing
- Admin functionality
- Product/order/user management application
