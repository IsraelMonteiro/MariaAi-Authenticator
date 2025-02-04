```markdown
# Token Adapter

Support for `ICRC1`, `ICRC2`, `EXT`, and `DIP20`

**Note:** The `approve` method is not implemented for `EXT` and `DIP20`.

## Overview

This module provides an easy-to-use interface for interacting with various token standards on the Internet Computer (IC). It supports common operations like querying balances, token metadata, and transferring tokens.

### Features

- Unified interface for multiple token standards.
- Support for `ICRC1`, `ICRC2`, `EXT`, and `DIP20` tokens.
- Asynchronous methods for efficient token interaction.
- Robust error handling for invalid token standards.

## Usage

```typescript
import { Token } from "@alpaca-icp/token-adapter";
import { HttpAgent } from "@dfinity/agent";

const agent = new HttpAgent({ host: "https://ic0.app" });

// Example for an ICP token
const token = new Token({
  canisterId: "ryjl3-tyaaa-aaaaa-aaaba-cai",
  agent,
  tokenStandard: "ICP",
});

await token.balanceOf("wallet");
await token.getLogo();

// Example for a DIP20 token
const Dip20_token = new Token({
  canisterId: "whdfs-saaaa-aaaao-awh4a-cai",
  agent,
  tokenStandard: "DIP20",
});
await Dip20_token.balanceOf("wallet");
await Dip20_token.getLogo();
```

## Supported Token Standards

- **EXT**: Extended Token Standard
- **DIP20**: DIP-20 Token Standard
- **ICRC1**: ICRC-1 Token Standard
- **ICRC2**: A combination of ICRC-1 and ICRC-2 standards
- **ICP**: ICPSwap standard for ICP tokens

## Token Interface

Below is the interface implemented by the `Token` class:

```typescript
export type ApproveInput = {
  fee: [] | [bigint];
  memo: [] | [Uint8Array | number[]];
  from_subaccount: [] | [Uint8Array | number[]];
  created_at_time: [] | [bigint];
  amount: bigint;
  expected_allowance: [] | [bigint];
  expires_at: [] | [bigint];
  spender: {
    owner: Principal;
    subaccount: [] | [Uint8Array | number[]];
  };
};

export type TransferInput = {
  to: {
    owner: Principal;
    subaccount: [] | [Uint8Array | number[]];
  };
  amount: bigint;
  fee: [bigint] | [];
  memo: [Uint8Array | number[]] | [];
  from_subaccount: [] | [Uint8Array | number[]];
  created_at_time: [bigint] | [];
};

export interface IToken {
  actor: TokenActor;
  getDecimals(): Promise<number>;
  balanceOf(
    address:
      | string
      | {
          owner: Principal;
          subaccount: [] | [Uint8Array | number[]];
        }
  ): Promise<number>;
  name(): Promise<string>;
  symbol(): Promise<string>;
  totalSupply(): Promise<number>;
  getFee(): Promise<bigint>;
  getMetadata(): Promise<any>;
  getLogo(): Promise<string>;
  /**
   * @description This method only works with EXT, ICRC2+ and DIP20 tokens
   */
  approve(input: ApproveInput): Promise<bigint>;

  transfer(input: TransferInput): Promise<bigint>;
}
```

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For questions or support, please refer to the [GitHub issues page](https://github.com/IsraelMonteiro/MariaAi-Authenticator).
```