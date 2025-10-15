from accounts import Account
import gradio as gr

def create_account(username, initial_deposit):
    global account
    account = Account(username, initial_deposit)
    return f"Account created for {username} with an initial deposit of ${initial_deposit}."

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited ${amount}. New balance: ${account.balance}."

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew ${amount}. New balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}. New balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}. New balance: ${account.balance}."
    except ValueError as e:
        return str(e)

def report_holdings():
    holdings = account.report_holdings()
    return holdings if holdings else "No holdings."

def report_profit_loss():
    profit_loss = account.report_profit_loss()
    return f"Profit/Loss: ${profit_loss}."

def list_transactions():
    transactions = account.list_transactions()
    return transactions if transactions else "No transactions."

with gr.Blocks() as demo:
    gr.Markdown("## Trading Simulation Account Management")
    with gr.Row():
        username = gr.Textbox(label="Username")
        initial_deposit = gr.Number(label="Initial Deposit", value=1000)
        create_btn = gr.Button("Create Account")
    
    create_output = gr.Textbox(label="Output")

    create_btn.click(create_account, inputs=[username, initial_deposit], outputs=create_output)

    with gr.Row():
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_btn = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Output")

    deposit_btn.click(deposit_funds, inputs=deposit_amount, outputs=deposit_output)

    with gr.Row():
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_btn = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Output")

    withdraw_btn.click(withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)

    with gr.Row():
        buy_symbol = gr.Textbox(label="Buy Symbol (AAPL, TSLA, GOOGL)")
        buy_quantity = gr.Number(label="Buy Quantity")
        buy_btn = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Output")

    buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

    with gr.Row():
        sell_symbol = gr.Textbox(label="Sell Symbol (AAPL, TSLA, GOOGL)")
        sell_quantity = gr.Number(label="Sell Quantity")
        sell_btn = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Output")

    sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Row():
        holdings_btn = gr.Button("Report Holdings")
        holdings_output = gr.Textbox(label="Holdings")

    holdings_btn.click(report_holdings, outputs=holdings_output)

    with gr.Row():
        profit_loss_btn = gr.Button("Report Profit/Loss")
        profit_loss_output = gr.Textbox(label="Profit/Loss")

    profit_loss_btn.click(report_profit_loss, outputs=profit_loss_output)

    with gr.Row():
        transactions_btn = gr.Button("List Transactions")
        transactions_output = gr.Textbox(label="Transactions")

    transactions_btn.click(list_transactions, outputs=transactions_output)

demo.launch()