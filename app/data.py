from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Prediction:
    horizon: str
    change_pct: float
    signal: str


@dataclass(frozen=True)
class ModelPrediction:
    name: str
    description: str
    predictions: List[Prediction]


MODEL_PREDICTIONS: List[ModelPrediction] = [
    ModelPrediction(
        name="GarudaVision Transformer",
        description="Hybrid transformer model blending macroeconomic indicators with price action for blue chips.",
        predictions=[
            Prediction("1-day", 1.8, "Buy"),
            Prediction("3-day", 4.1, "Buy"),
            Prediction("1-week", 5.6, "Buy"),
        ],
    ),
    ModelPrediction(
        name="BatikFlow LSTM",
        description="Stacked LSTM tuned on IDX30 liquidity patterns with adaptive learning rate scheduling.",
        predictions=[
            Prediction("1-day", -0.9, "Sell"),
            Prediction("3-day", 0.6, "Hold"),
            Prediction("1-week", 2.4, "Buy"),
        ],
    ),
    ModelPrediction(
        name="Nusantara Prophet+",
        description="Prophet ensemble augmented with sentiment scoring from Indonesian financial news feeds.",
        predictions=[
            Prediction("1-day", 0.7, "Buy"),
            Prediction("3-day", 1.9, "Buy"),
            Prediction("1-week", 3.5, "Buy"),
        ],
    ),
    ModelPrediction(
        name="JakartaWaveNet",
        description="Dilated causal CNN capturing intraday volatility clusters for export-heavy sectors.",
        predictions=[
            Prediction("1-day", -1.2, "Sell"),
            Prediction("3-day", -0.4, "Sell"),
            Prediction("1-week", 0.9, "Hold"),
        ],
    ),
    ModelPrediction(
        name="Komodo RL Trader",
        description="Reinforcement learning agent optimizing reward on simulated IDX order books.",
        predictions=[
            Prediction("1-day", 2.1, "Buy"),
            Prediction("3-day", 3.8, "Buy"),
            Prediction("1-week", 6.2, "Buy"),
        ],
    ),
    ModelPrediction(
        name="Archipelago Gradient Boost",
        description="Gradient boosting model fusing commodity prices with sector ETF flows.",
        predictions=[
            Prediction("1-day", 0.3, "Hold"),
            Prediction("3-day", 1.4, "Buy"),
            Prediction("1-week", 2.7, "Buy"),
        ],
    ),
    ModelPrediction(
        name="SpiceRoute Meta-Learner",
        description="Meta-learner stacking ridge regression, SVR, and attention networks for resilient forecasts.",
        predictions=[
            Prediction("1-day", -0.5, "Sell"),
            Prediction("3-day", 0.8, "Buy"),
            Prediction("1-week", 1.1, "Buy"),
        ],
    ),
    ModelPrediction(
        name="Merapi Volatility Net",
        description="Volatility-conditioned transformer adapting to commodity-driven market swings.",
        predictions=[
            Prediction("1-day", 1.1, "Buy"),
            Prediction("3-day", 2.6, "Buy"),
            Prediction("1-week", 3.9, "Buy"),
        ],
    ),
    ModelPrediction(
        name="SelatGAN Forecaster",
        description="Generative adversarial network synthesizing scenario-based futures for financial planning.",
        predictions=[
            Prediction("1-day", -1.5, "Sell"),
            Prediction("3-day", 0.2, "Hold"),
            Prediction("1-week", 1.6, "Buy"),
        ],
    ),
    ModelPrediction(
        name="Riau GraphSAGE Agent",
        description="Graph neural network leveraging supply-chain relationships among IDX listings.",
        predictions=[
            Prediction("1-day", 0.9, "Buy"),
            Prediction("3-day", 1.5, "Buy"),
            Prediction("1-week", 2.2, "Buy"),
        ],
    ),
]
