# Python ELK Stack Application

This repository contains a simple Python application that sends logs to an ELK (Elasticsearch, Logstash, Kibana) stack for log collection, storage, and visualization.

## Project Structure

```
.
├── app.py                   # Python application that generates and sends logs
├── docker-compose.yml       # Docker Compose configuration for ELK stack
├── elasticsearch/
│   └── elasticsearch.yml    # Elasticsearch configuration
├── kibana/
│   └── kibana.yml           # Kibana configuration
└── logstash/
    ├── logstash.conf        # Logstash pipeline configuration
    └── logstash.yml         # Logstash server configuration
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3

### Running the ELK Stack

1. Start the ELK stack using Docker Compose:

```bash
docker-compose up -d
```

2. Wait for all services to start (this may take a minute or two):

```bash
docker-compose ps
```

All services should show as "Up" status.

### Sending Logs

To send sample logs to the ELK stack, run the Python application:

```bash
python3 app.py [number_of_logs]
```

Where `[number_of_logs]` is an optional parameter specifying how many logs to send (default is 20).

## Creating a Data View in Kibana

To visualize your logs in Kibana, you need to create a data view. Follow these steps:

1. **Access Kibana**: 
   Open your web browser and navigate to [http://localhost:5601](http://localhost:5601)

2. **Navigate to Data Views**:
   - Click on the hamburger menu (☰) in the top left corner
   - Click on "Stack Management" (usually near the bottom of the menu)
   - Under "Kibana", click on "Data Views"

3. **Create a New Data View**:
   - Click the "Create data view" button in the top right
   - In the "Name" field, enter a name for your data view (e.g., "logstash-logs")
   - In the "Index pattern" field, enter `logs-generic-default*` (this matches the index where Logstash is storing your logs)
   - For "Timestamp field", select `@timestamp` from the dropdown
   - Click "Save data view to Kibana" at the bottom of the form

4. **Verify Data View Creation**:
   - Your new data view should appear in the list of data views
   - Click on the data view name to see the available fields and their types

5. **View Your Logs**:
   - Go back to the main Kibana menu by clicking on the Kibana logo in the top left
   - Click on "Discover" in the left navigation
   - Select your new data view from the dropdown in the top left of the Discover page
   - You should now see your logs visualized in Kibana

## Creating Visualizations

After creating your data view, you can create visualizations:

1. Go to "Visualize Library" from the left navigation menu
2. Click "Create new visualization"
3. Select a visualization type (e.g., Line, Bar, Pie, etc.)
4. Select your data view
5. Configure your visualization using the available fields:
   - `level`: Use for filtering or as a breakdown to see distribution of log levels
   - `service`: Use to analyze logs by service
   - `message`: Contains the actual log message
   - `request_id`: Unique identifier for tracking related logs
   - `processing_time_ms`: Metric field useful for performance analysis

## Creating a Dashboard

To create a dashboard combining multiple visualizations:

1. Go to "Dashboard" from the left navigation menu
2. Click "Create new dashboard"
3. Click "Add" and then "Add visualization" to add your saved visualizations
4. Arrange and resize visualizations as needed
5. Save your dashboard with a descriptive name

## Troubleshooting

- **No logs showing in Kibana**: Check that Logstash is properly receiving and forwarding logs to Elasticsearch by examining its logs: `docker logs logstash`
- **Connection refused errors**: Ensure all services are running with `docker-compose ps` and that proper ports are open
- **Parsing errors**: Verify the JSON format in your logs matches what Logstash expects in its configuration

## Additional Resources

- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Logstash Documentation](https://www.elastic.co/guide/en/logstash/current/index.html)
- [Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)
