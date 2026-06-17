# Solana Whale Tracker — Core Transaction Monitor

A high-performance, asynchronous Python script designed to interface directly with the Solana blockchain via RPC nodes to monitor and fetch real-time transaction signatures and block slots for designated wallet addresses. 

This project serves as Phase 1 of a sovereign protocol intelligence infrastructure stack, shifting away from abstracted third-party APIs to establish direct data optics.

## Features

- **Async Architecture:** Powered by `asyncio` and `solana-py` to ensure non-blocking network I/O when communicating with the cluster.
- **Robust Type Safety:** Leverages Rust-backed `solders` bindings for reliable public key validation and cryptographic address parsing.
- **Dual Execution Modes:** Accepts public keys dynamically via command-line arguments or through a secure runtime fallback prompt.
- **Clean Execution Flow:** Structured exception handling with guaranteed connection-pool termination (`finally` blocks) to prevent resource leaks.

## Prerequisites

Ensure your environment is running Python 3.10+ and install the modern Solana core libraries:

```bash
pip install solana solders
