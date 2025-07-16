# Dockerfile to build the validmind-docs image

# Use the official Nginx image
FROM nginx:stable-alpine

# Install jq for JSON parsing
RUN apk add --no-cache jq bash

# Security Upgrade Zone
RUN apk upgrade --no-cache libxml2

# Copy the built static site
COPY _site /usr/share/nginx/html

# Copy config.json for fallback values
COPY config.json /usr/share/nginx/html/

# Copy the entrypoint script
COPY scripts/docker_entrypoint.sh /

# Make the entrypoint script executable
RUN chmod +x /docker_entrypoint.sh

# Use our custom entrypoint
ENTRYPOINT ["/docker_entrypoint.sh"]

# Default command
CMD ["nginx", "-g", "daemon off;"]
