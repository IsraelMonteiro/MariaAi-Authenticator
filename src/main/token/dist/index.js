"use strict";

// Helper function to handle async/await pattern
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};

// Required imports for token standards
const dip20_1 = require("./dip20"); // DIP20 Token implementation
const icrc1_1 = require("./icrc1"); // ICRC1 Token implementation
const ext_1 = require("./ext"); // EXT Token implementation

// Token class: A universal interface for managing different token standards
class Token {
    /**
     * Token Constructor
     * @param {Object} params - Configuration for initializing a token instance
     * @param {string} params.canisterId - Canister ID of the token
     * @param {HttpAgent} params.agent - Agent for communication with the Internet Computer
     * @param {string} params.tokenStandard - The token standard (DIP20, EXT, ICRC1, etc.)
     */
    constructor({ canisterId, agent, tokenStandard }) {
        switch (tokenStandard) {
            case "DIP20":
                this.token = new dip20_1.Dip20Token({
                    canisterId,
                    agent,
                });
                break;
            case "EXT":
                this.token = new ext_1.ExtToken({
                    canisterId,
                    agent,
                });
                break;
            case "ICRC1":
            case "ICRC2":
            case "ICP":
                this.token = new icrc1_1.ICRC1Token({
                    agent,
                    canisterId,
                });
                break;
            default:
                throw new Error("Invalid token standard");
        }
    }

    /**
     * Get the number of decimals for the token.
     * @returns {Promise<number>} Number of decimals
     */
    getDecimals() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.getDecimals();
        });
    }

    /**
     * Get the balance of a specific address.
     * @param {string | Object} address - Address to check the balance
     * @returns {Promise<number>} Balance of the address
     */
    balanceOf(address) {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.balanceOf(address);
        });
    }

    /**
     * Get the token name.
     * @returns {Promise<string>} Token name
     */
    name() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.name();
        });
    }

    /**
     * Get the token symbol.
     * @returns {Promise<string>} Token symbol
     */
    symbol() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.symbol();
        });
    }

    /**
     * Get the total supply of the token.
     * @returns {Promise<number>} Total supply
     */
    totalSupply() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.totalSupply();
        });
    }

    /**
     * Get the transaction fee for the token.
     * @returns {Promise<bigint>} Fee amount
     */
    getFee() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.getFee();
        });
    }

    /**
     * Get the metadata of the token.
     * @returns {Promise<any>} Metadata information
     */
    getMetadata() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.getMetadata();
        });
    }

    /**
     * Get the logo of the token.
     * @returns {Promise<string>} Logo URL or base64 string
     */
    getLogo() {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.getLogo();
        });
    }

    /**
     * Approve a spender to use a specified amount of tokens.
     * @param {ApproveInput} input - Approval details
     * @returns {Promise<bigint>} Approval result
     */
    approve(input) {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.approve(input);
        });
    }

    /**
     * Transfer tokens to another account.
     * @param {TransferInput} input - Transfer details
     * @returns {Promise<bigint>} Transfer result
     */
    transfer(input) {
        return __awaiter(this, void 0, void 0, function* () {
            return this.token.transfer(input);
        });
    }
}

exports.Token = Token;

// Log message to confirm the module initialization
console.log("Token module initialized successfully!");
