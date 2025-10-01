def adoption_curve(innovation: float, market_size: float, imitation: float, penetration_start: float) -> float:
    """
    Calculates the adoption curve based on the Bass diffusion model.

    Parameters:
        innovation (float): The innovation coefficient (p).
        market_size (float): The total market size.
        imitation (float): The imitation coefficient (q).
        penetration_start (float): The current market penetration.

    Returns:
        float: The rate of adoption.
    """
    adoption_rate = (
        innovation * (market_size - penetration_start) +
        imitation * (penetration_start / market_size) * (market_size - penetration_start)
    )
    return adoption_rate