# CNCF Issue Tracker Configuration
# Edit this file to customize your bot settings

# Your 10 repositories to monitor (format: "owner/repo")
REPOSITORIES = [
    "litmuschaos/litmus",
    "litmuschaos/litmus-docs",
    "litmuschaos/website-litmuschaos",
    "knative/docs",
    "knative/website",
    "knative/community",
    "knative-extensions/kn-plugin-quickstart",
    "antrea-io/antrea",
    "antrea-io/antrea-ui",
    "antrea-io/antrea "
]

# Check interval in seconds (60-240 seconds = 1-4 minutes)
DEFAULT_CHECK_INTERVAL = 180  # 3 minutes

# Database file path
DATABASE_PATH = "cncf_issues.db"

# Logging level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL = "INFO"

# Batch size for processing repositories (to avoid overwhelming APIs)
BATCH_SIZE = 3

# Delay between batches in seconds
BATCH_DELAY = 2

# Rate limiting delay between issue notifications in seconds
NOTIFICATION_DELAY = 1

# Timeout for API requests in seconds
API_TIMEOUT = 10

# Buffer time for issue checking (minutes added to check interval)
CHECK_BUFFER_MINUTES = 2