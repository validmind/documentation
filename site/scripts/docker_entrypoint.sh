#!/bin/sh
# Script to replace placeholders with actual URLs in HTML files and search.json

set -e

echo "==== Start ValidMind URL configuration ===="

# Define paths
MANIFEST_FILE="/usr/share/nginx/html/validmind-docs.yaml"
HTML_DIR="/usr/share/nginx/html"

# Define placeholder values, same as in make_site_configurable.sh
VALIDMIND_PLACEHOLDER="https://app.prod.validmind-configurable-url.ai"
JUPYTERHUB_PLACEHOLDER="https://jupyterhub.validmind-configurable-url.ai"
PRODUCT_PLACEHOLDER="CONFIGURABLE_PRODUCT_NAME"

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

# Function to extract value from YAML manifest
extract_yaml_value() {
    local key="$1"
    local file="$2"
    
    # Extract simple key-value pairs
    if [ "$key" = "VALIDMIND_URL" ] || [ "$key" = "JUPYTERHUB_URL" ] || [ "$key" = "PRODUCT_NAME" ]; then
        grep "^[[:space:]]*${key}:" "$file" 2>/dev/null | sed "s/^[[:space:]]*${key}:[[:space:]]*//;s/[\"']//g"
    # Extract multiline YAML values (for SVG content)
    elif [ "$key" = "LOGO_SVG" ] || [ "$key" = "FAVICON_SVG" ]; then
        awk "
        /^[[:space:]]*${key}:[[:space:]]*\|/ { 
            in_block=1; 
            next 
        } 
        in_block && /^[[:space:]]*[A-Z_]+:/ { 
            in_block=0 
        } 
        in_block && /^    / { 
            sub(/^    /, \"\"); 
            print 
        }
        " "$file" 2>/dev/null
    fi
}

# If still empty, try manifest file
if { [ -z "$VALIDMIND_URL" ] || [ -z "$JUPYTERHUB_URL" ] || [ -z "$PRODUCT_NAME" ] || [ -z "$LOGO_SVG" ] || [ -z "$FAVICON_SVG" ]; } && [ -f "$MANIFEST_FILE" ]; then
    echo "Looking for values in manifest file: $MANIFEST_FILE"
    
    [ -z "$VALIDMIND_URL" ] && VALIDMIND_URL=$(extract_yaml_value "VALIDMIND_URL" "$MANIFEST_FILE")
    [ -z "$JUPYTERHUB_URL" ] && JUPYTERHUB_URL=$(extract_yaml_value "JUPYTERHUB_URL" "$MANIFEST_FILE")
    [ -z "$PRODUCT_NAME" ] && PRODUCT_NAME=$(extract_yaml_value "PRODUCT_NAME" "$MANIFEST_FILE")
    [ -z "$LOGO_SVG" ] && LOGO_SVG=$(extract_yaml_value "LOGO_SVG" "$MANIFEST_FILE")
    [ -z "$FAVICON_SVG" ] && FAVICON_SVG=$(extract_yaml_value "FAVICON_SVG" "$MANIFEST_FILE")
    
    [ -n "$VALIDMIND_URL" ] && echo "Using VALIDMIND_URL from manifest: $VALIDMIND_URL"
    [ -n "$JUPYTERHUB_URL" ] && echo "Using JUPYTERHUB_URL from manifest: $JUPYTERHUB_URL"
    [ -n "$PRODUCT_NAME" ] && echo "Using PRODUCT_NAME from manifest: $PRODUCT_NAME"
    [ -n "$LOGO_SVG" ] && echo "Using LOGO_SVG from manifest: $(echo "$LOGO_SVG" | wc -c) characters"
    [ -n "$FAVICON_SVG" ] && echo "Using FAVICON_SVG from manifest: $(echo "$FAVICON_SVG" | wc -c) characters"
fi

# Finally, use hardcoded defaults as a last resort
if [ -z "$VALIDMIND_URL" ]; then
    VALIDMIND_URL="https://app.prod.validmind.ai"
    echo "INFO: Using default VALIDMIND_URL: $VALIDMIND_URL"
fi

if [ -z "$JUPYTERHUB_URL" ]; then
    JUPYTERHUB_URL="https://jupyterhub.validmind.ai"
    echo "INFO: Using default JUPYTERHUB_URL: $JUPYTERHUB_URL"
fi

if [ -z "$PRODUCT_NAME" ]; then
    PRODUCT_NAME="ValidMind AI Risk Platform"
    echo "INFO: Using default PRODUCT_NAME: $PRODUCT_NAME"
fi

if [ -z "$LOGO_SVG" ]; then
    echo "INFO: Using original logo."
fi

if [ -z "$FAVICON_SVG" ]; then
    echo "INFO: Using original favicon."
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
