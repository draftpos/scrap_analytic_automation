# Scrap & Transfer Analytic Automation

## Overview

The **Scrap & Transfer Analytic Automation** module for Odoo allows you to seamlessly apply analytic distributions from Internal Transfers and Scrap Orders directly to their resulting journal entries (Inventory Valuation). 

By default, Odoo's stock valuation entries may not carry over analytic distributions effectively. This module bridges that gap by ensuring that the analytic distribution set at the header or line level of your transfers and scrap orders is correctly applied to the generated accounting moves.

## Features

- **Automated Analytic Distribution**: Propagates analytic distributions from `stock.picking` (Internal Transfers) and `stock.scrap` (Scrap Orders) to the resulting `account.move.line` entries.
- **Smart Account Filtering**: The module intelligently filters which journal items receive the analytic distribution. It only applies the distribution to specific Profit & Loss account types:
  - **Expenses** (`expense`)
  - **Cost of Revenue** (`expense_direct_cost`)
  - **Income** (`income`)
  - **Other Income** (`income_other`)
- **Clean Accounting**: By filtering the target accounts, it ensures that balance sheet accounts like *Stock Valuation* or *Payables* are kept clean and are not polluted with unnecessary analytic distributions.

## Usage

1. Create an **Internal Transfer** or a **Scrap Order**.
2. Set the **Analytic Distribution** on the operation lines or at the header level.
3. Validate the transfer or scrap order.
4. Check the generated **Inventory Valuation** journal entry. You will see that the analytic distribution has been correctly applied only to the P&L accounts (e.g., Cost of Goods Sold, Stock Variation), leaving the Stock Valuation account untouched.

## Technical Details

- **Depends on**: `base`, `stock`, `account`, `stock_account`, `analytic`
- **Models Extended**: 
  - `stock.move`
  - `stock.picking`
  - `stock.scrap`
  - `account.move`

## License

This module is licensed under LGPL-3.
