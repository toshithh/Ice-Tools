#!/usr/bin/env bash

hash="$1"

# Extract fields using regex-like matching
if [[ "$hash" =~ ^pbkdf2:sha256:([0-9]+)\$([^$]+)\$(.*)$ ]]; then
    iterations="${BASH_REMATCH[1]}"
    salt="${BASH_REMATCH[2]}"
    hash1="${BASH_REMATCH[3]}"
else
    echo "Input format not recognized" >&2
    exit 1
fi

# Base64 encode the salt
salt_b64=$(printf "%s" "$salt" | base64)

# Decode hex hash then Base64 encode
hash_b64=$(printf "%s" "$hash1" | xxd -r -p | base64)

echo "sha256:$iterations:$salt_b64:$hash_b64"