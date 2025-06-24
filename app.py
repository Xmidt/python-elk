import socket
import time
import json
import logging
import random
import sys

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def send_log(message, host='localhost', port=5000):
    """Send a log message to Logstash via TCP."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        # Add newline to ensure message is properly delimited
        message_with_newline = message + '\n'
        sock.sendall(message_with_newline.encode('utf-8'))
        logger.info(f"Sent log: {message}")
        sock.close()
    except Exception as e:
        logger.error(f"Error sending log: {str(e)}")

def generate_log():
    """Generate a sample log message in JSON format."""
    log_levels = ['INFO', 'WARN', 'ERROR', 'DEBUG']
    services = ['user-service', 'payment-service', 'order-service', 'inventory-service']
    messages = [
        'Request processed successfully',
        'Database connection timeout',
        'Payment verification failed',
        'User login successful',
        'Cache invalidated',
        'API rate limit exceeded'
    ]
    
    log_entry = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S.%fZ', time.gmtime()),
        'level': random.choice(log_levels),
        'service': random.choice(services),
        'message': random.choice(messages),
        'request_id': f'req-{random.randint(1000, 9999)}',
        'processing_time_ms': random.randint(1, 500)
    }
    
    return json.dumps(log_entry)

if __name__ == "__main__":
    logger.info("Starting to send logs to Logstash...")
    
    num_logs = 20
    if len(sys.argv) > 1:
        try:
            num_logs = int(sys.argv[1])
        except ValueError:
            pass
    
    for i in range(num_logs):
        log_message = generate_log()
        send_log(log_message)
        time.sleep(0.5)  # Small delay between logs
    
    logger.info(f"Finished sending {num_logs} logs to Logstash.")
