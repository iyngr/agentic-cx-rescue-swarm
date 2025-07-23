def refund_tool(order_id: str, amount: float) -> dict:
    """
    Issues a refund for a given order.

    Args:
        order_id: The ID of the order to refund.
        amount: The amount to refund.

    Returns:
        A dictionary with the refund status.
    """
    # In a real implementation, this would call a payment gateway API.
    # For this example, we'll use mock data.
    print(f"Refund of ${amount} for order {order_id} processed successfully.")
    return {"status": "success"}

def reship_order_tool(order_id: str) -> dict:
    """
    Re-ships a given order.

    Args:
        order_id: The ID of the order to re-ship.

    Returns:
        A dictionary with the re-shipment status.
    """
    # In a real implementation, this would call a logistics API.
    # For this example, we'll use mock data.
    print(f"Re-shipment for order {order_id} processed successfully.")
    return {"status": "success"}

def generate_coupon_tool(value: int, unit: str) -> dict:
    """
    Generates a coupon for a customer.

    Args:
        value: The value of the coupon.
        unit: The unit of the coupon (e.g., "percent", "dollars").

    Returns:
        A dictionary with the coupon code.
    """
    # In a real implementation, this would call a coupon generation API.
    # For this example, we'll use mock data.
    coupon_code = "WELCOME50" if unit == "percent" else "WELCOME10"
    print(f"Coupon for {value}{unit} generated successfully: {coupon_code}")
    return {"coupon_code": coupon_code}

def send_communication_tool(recipient: str, channel: str, body: str) -> dict:
    """
    Sends a communication to a customer.

    Args:
        recipient: The recipient of the communication.
        channel: The channel of the communication (e.g., "email", "sms").
        body: The body of the communication.

    Returns:
        A dictionary with the communication status.
    """
    # In a real implementation, this would call an email or SMS API.
    # For this example, we'll use mock data.
    print(f"Communication sent to {recipient} via {channel}: {body}")
    return {"status": "success"}

def log_to_crm_tool(customer_id: str, log_entry: str) -> dict:
    """
    Logs an incident and resolution in the CRM.

    Args:
        customer_id: The ID of the customer.
        log_entry: The log entry to add to the customer's record.

    Returns:
        A dictionary with the logging status.
    """
    # In a real implementation, this would call a CRM API.
    # For this example, we'll use mock data.
    print(f"Log entry for customer {customer_id} added to CRM: {log_entry}")
    return {"status": "success"}
