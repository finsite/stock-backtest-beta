"""
Processor module for stock-backtest-beta signal generation.

Validates incoming messages and computes beta signals based on
historical price data. All operations are logged for observability.
"""

from typing import Any

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """
    Validate the incoming raw message against the expected schema.

    Args:
        message (dict[str, Any]): The raw message payload.

    Returns:
        ValidatedMessage: A validated message object.

    Raises:
        ValueError: If the message format is invalid.
    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Invalid message schema: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def compute_beta_signal(message: ValidatedMessage) -> dict[str, Any]:
    """
    Compute a beta signal from the validated input message.

    Placeholder implementation. A real version would use historical
    correlation and variance vs. a benchmark (e.g., S&P 500).

    Args:
        message (ValidatedMessage): The validated input data.

    Returns:
        dict[str, Any]: The enriched message with beta signal.
    """
    symbol = message.get("symbol", "UNKNOWN")
    logger.info("📈 Computing beta signal for %s", symbol)

    # Placeholder beta signal (normally: covariance(stock, market) / var(market))
    beta_value = 1.05  # pretend this is calculated
    signal = "OVEREXPOSED" if beta_value > 1.0 else "UNDEREXPOSED"

    result = {
        "beta": beta_value,
        "beta_signal": signal,
    }

    logger.debug("✅ Computed beta signal for %s: %s", symbol, result)
    return {**message, **result}
