#!/bin/sh
# Script to replace placeholders with actual URLs in HTML files and search.json

set -e

echo "==== Start ValidMind URL configuration ===="

# Define paths
CONFIG_FILE="/usr/share/nginx/html/config.json"
HTML_DIR="/usr/share/nginx/html"

# Define placeholder values, same as in make_site_configurable.sh
VALIDMIND_PLACEHOLDER="https://app.prod.validmind-configurable-url.ai"
JUPYTERHUB_PLACEHOLDER="https://jupyterhub.validmind-configurable-url.ai"
PRODUCT_PLACEHOLDER="CONFIGURABLE_PRODUCT_NAME"
LOGO_PLACEHOLDER="VALIDMIND_LOGO_SVG_PLACEHOLDER"
FAVICON_PLACEHOLDER="VALIDMIND_FAVICON_SVG_PLACEHOLDER"

echo "Initializing ValidMind documentation site..."

# Initialize variables as empty
VALIDMIND_URL=""
JUPYTERHUB_URL=""
PRODUCT_NAME=""
LOGO_SVG=""
FAVICON_SVG=""

# First check environment variables
if [ -n "${VALIDMIND_URL:-}" ]; then
    VALIDMIND_URL="$VALIDMIND_URL"
    echo "Using VALIDMIND_URL from environment: $VALIDMIND_URL"
fi

if [ -n "${JUPYTERHUB_URL:-}" ]; then
    JUPYTERHUB_URL="$JUPYTERHUB_URL"
    echo "Using JUPYTERHUB_URL from environment: $JUPYTERHUB_URL"
fi

if [ -n "${PRODUCT_NAME:-}" ]; then
    PRODUCT_NAME="$PRODUCT_NAME"
    echo "Using PRODUCT_NAME from environment: $PRODUCT_NAME"
fi

if [ -n "${LOGO_SVG:-}" ]; then
    LOGO_SVG="$LOGO_SVG"
    echo "Using LOGO_SVG from environment: $(echo "$LOGO_SVG" | wc -c) characters"
fi

if [ -n "${FAVICON_SVG:-}" ]; then
    FAVICON_SVG="$FAVICON_SVG"
    echo "Using FAVICON_SVG from environment: $(echo "$FAVICON_SVG" | wc -c) characters"
fi

# If still empty, try config.json
if { [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ] || [ -z "$PRODUCT_NAME" ] || [ -z "$LOGO_SVG" ] || [ -z "$FAVICON_SVG" ]; } && [ -f "$CONFIG_FILE" ]; then
    echo "Looking for values in config file: $CONFIG_FILE"
    
    if command -v jq > /dev/null 2>&1; then
        # Use jq if available
        [ -z "$VALIDMIND_URL" ] && VALIDMIND_URL=$(jq -r '.VALIDMIND_URL // empty' "$CONFIG_FILE")
        [ -z "$JUPYTERHUB_URL" ] && JUPYTERHUB_URL=$(jq -r '.JUPYTERHUB_URL // empty' "$CONFIG_FILE")
        [ -z "$PRODUCT_NAME" ] && PRODUCT_NAME=$(jq -r '.PRODUCT_NAME // empty' "$CONFIG_FILE")
        [ -z "$LOGO_SVG" ] && LOGO_SVG=$(jq -r '.LOGO_SVG // empty' "$CONFIG_FILE")
        [ -z "$FAVICON_SVG" ] && FAVICON_SVG=$(jq -r '.FAVICON_SVG // empty' "$CONFIG_FILE")
    else
        # Simple fallback if jq isn't available
        [ -z "$VALIDMIND_URL" ] && VALIDMIND_URL=$(grep -o '"VALIDMIND_URL":"[^"]*"' "$CONFIG_FILE" 2>/dev/null | sed 's/"VALIDMIND_URL":"//;s/"//g')
        [ -z "$JUPYTERHUB_URL" ] && JUPYTERHUB_URL=$(grep -o '"JUPYTERHUB_URL":"[^"]*"' "$CONFIG_FILE" 2>/dev/null | sed 's/"JUPYTERHUB_URL":"//;s/"//g')
        [ -z "$PRODUCT_NAME" ] && PRODUCT_NAME=$(grep -o '"PRODUCT_NAME":"[^"]*"' "$CONFIG_FILE" 2>/dev/null | sed 's/"PRODUCT_NAME":"//;s/"//g')
        # Note: SVG extraction via grep is complex due to multiline content and special characters
        # If jq is not available and SVG content is needed, consider installing jq in the Docker image
        if [ -z "$LOGO_SVG" ]; then
            echo "Warning: jq not available for LOGO_SVG extraction. Install jq for full functionality."
        fi
        if [ -z "$FAVICON_SVG" ]; then
            echo "Warning: jq not available for FAVICON_SVG extraction. Install jq for full functionality."
        fi
    fi
    
    [ -n "$VALIDMIND_URL" ] && echo "Using VALIDMIND_URL from config: $VALIDMIND_URL"
    [ -n "$JUPYTERHUB_URL" ] && echo "Using JUPYTERHUB_URL from config: $JUPYTERHUB_URL"
    [ -n "$PRODUCT_NAME" ] && echo "Using PRODUCT_NAME from config: $PRODUCT_NAME"
    [ -n "$LOGO_SVG" ] && echo "Using LOGO_SVG from config: $(echo "$LOGO_SVG" | wc -c) characters"
    [ -n "$FAVICON_SVG" ] && echo "Using FAVICON_SVG from config: $(echo "$FAVICON_SVG" | wc -c) characters"
fi

# Finally, use hardcoded defaults as a last resort
if [ -z "$VALIDMIND_URL" ]; then
    VALIDMIND_URL="https://app.prod.validmind.ai"
    echo "Using default VALIDMIND_URL: $VALIDMIND_URL"
fi

if [ -z "$JUPYTERHUB_URL" ]; then
    JUPYTERHUB_URL="https://jupyterhub.validmind.ai"
    echo "Using default JUPYTERHUB_URL: $JUPYTERHUB_URL"
fi

if [ -z "$PRODUCT_NAME" ]; then
    PRODUCT_NAME="&#8203;ValidMind"
    echo "Using default PRODUCT_NAME: $PRODUCT_NAME"
fi

if [ -z "$LOGO_SVG" ]; then
    echo "Warning: No LOGO_SVG provided. Using placeholder."
fi

if [ -z "$FAVICON_SVG" ]; then
    echo "Warning: No FAVICON_SVG provided. Using placeholder."
fi

# Final check to ensure we have non-empty values for required parameters
if [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ] || [ -z "$PRODUCT_NAME" ]; then
    echo "Error: One or more required configuration values are still empty. This will cause replacement issues."
    exit 1
fi

# Count total placeholder instances
VALIDMIND_COUNT=$(grep -r "$VALIDMIND_PLACEHOLDER" "$HTML_DIR" | wc -l)
JUPYTERHUB_COUNT=$(grep -r "$JUPYTERHUB_PLACEHOLDER" "$HTML_DIR" | wc -l)
PRODUCT_COUNT=$(grep -r "$PRODUCT_PLACEHOLDER" "$HTML_DIR" | wc -l)
echo "Found placeholders:"
echo "$VALIDMIND_COUNT instances of $VALIDMIND_PLACEHOLDER"
echo "$JUPYTERHUB_COUNT instances of $JUPYTERHUB_PLACEHOLDER"
echo "$PRODUCT_COUNT instances of $PRODUCT_PLACEHOLDER"

# Replace placeholders in HTML files
echo "Replacing URL placeholders in HTML files..."
find "$HTML_DIR" -type f -name "*.html" -exec sed -i "s|$VALIDMIND_PLACEHOLDER|$VALIDMIND_URL|g" {} \;
find "$HTML_DIR" -type f -name "*.html" -exec sed -i "s|$JUPYTERHUB_PLACEHOLDER|$JUPYTERHUB_URL|g" {} \;

echo "Replacing product name placeholders in HTML files..."
find "$HTML_DIR" -type f -name "*.html" -exec sed -i "s|$PRODUCT_PLACEHOLDER|$PRODUCT_NAME|g" {} \;

# Replace SVG content with actual SVG files if provided
if [ -n "$LOGO_SVG" ]; then
    echo "Replacing logo.svg with custom content..."
    echo "$LOGO_SVG" > "$HTML_DIR/logo.svg"
fi

if [ -n "$FAVICON_SVG" ]; then
    echo "Replacing favicon.svg with custom content..."
    echo "$FAVICON_SVG" > "$HTML_DIR/favicon.svg"
fi

# Replace placeholders in search.json file
echo "Replacing placeholders in search.json..."
if [ -f "$HTML_DIR/search.json" ]; then
    sed -i "s|$VALIDMIND_PLACEHOLDER|$VALIDMIND_URL|g" "$HTML_DIR/search.json"
    sed -i "s|$JUPYTERHUB_PLACEHOLDER|$JUPYTERHUB_URL|g" "$HTML_DIR/search.json"
    sed -i "s|$PRODUCT_PLACEHOLDER|$PRODUCT_NAME|g" "$HTML_DIR/search.json"
else
    echo "search.json file not found"
fi

# Verify replacement
VALIDMIND_AFTER=$(grep -r "$VALIDMIND_PLACEHOLDER" "$HTML_DIR" | wc -l)
JUPYTERHUB_AFTER=$(grep -r "$JUPYTERHUB_PLACEHOLDER" "$HTML_DIR" | wc -l)
PRODUCT_AFTER=$(grep -r "$PRODUCT_PLACEHOLDER" "$HTML_DIR" | wc -l)
echo "After replacement:"
echo "$VALIDMIND_AFTER instances of $VALIDMIND_PLACEHOLDER"
echo "$JUPYTERHUB_AFTER instances of $JUPYTERHUB_PLACEHOLDER"
echo "$PRODUCT_AFTER instances of $PRODUCT_PLACEHOLDER"

if [ "$VALIDMIND_AFTER" -eq 0 ] && [ "$JUPYTERHUB_AFTER" -eq 0 ] && [ "$PRODUCT_AFTER" -eq 0 ]; then
    echo "✓ All placeholder replacements completed successfully"
else
    echo "⚠ Some placeholders might not have been replaced"
    echo "Files still containing placeholders:"
    grep -l "$VALIDMIND_PLACEHOLDER\|$JUPYTERHUB_PLACEHOLDER\|$PRODUCT_PLACEHOLDER" "$HTML_DIR" | head -5
fi

echo "==== URL configuration complete ===="
