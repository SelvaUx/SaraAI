use anyhow::Result;
use clap::Parser;
use std::net::SocketAddr;
use tracing::{info, error};
use warp::Filter;

mod config;
mod database;
mod search;
mod server;
mod models;

use crate::config::Config;
use crate::database::Database;
use crate::search::SearchEngine;
use crate::server::create_routes;

#[derive(Parser, Debug)]
#[command(name = "knowledge-server")]
#[command(about = "📚 SaraAI Knowledge Base and Search Server")]
#[command(version = "1.0.0")]
struct Args {
    /// Host to bind to
    #[arg(short, long, default_value = "127.0.0.1")]
    host: String,

    /// Port to listen on  
    #[arg(short, long, default_value = "8004")]
    port: u16,

    /// Configuration file path
    #[arg(short, long)]
    config: Option<String>,

    /// Database path
    #[arg(short, long, default_value = "database/knowledge.db")]
    database: String,

    /// Search index path
    #[arg(short, long, default_value = "database/search_index")]
    index: String,

    /// Enable verbose logging
    #[arg(short, long)]
    verbose: bool,
}

#[tokio::main]
async fn main() -> Result<()> {
    let args = Args::parse();

    // Initialize tracing
    let log_level = if args.verbose { "debug" } else { "info" };
    tracing_subscriber::fmt()
        .with_env_filter(format!("saraai_knowledge={},knowledge_server={}", log_level, log_level))
        .init();

    info!("📚 Starting SaraAI Knowledge Base and Search Server v1.0.0");
    info!("===========================================================");

    // Load configuration
    let config = if let Some(config_path) = args.config {
        Config::from_file(&config_path)?
    } else {
        Config::default()
    };

    info!("⚙️ Configuration:");
    info!("  Database: {}", args.database);
    info!("  Search Index: {}", args.index);
    info!("  Host: {}", args.host);
    info!("  Port: {}", args.port);

    // Initialize database
    info!("🗄️ Initializing database...");
    let database = Database::new(&args.database).await?;
    info!("✅ Database initialized successfully");

    // Initialize search engine
    info!("🔍 Initializing search engine...");
    let search_engine = SearchEngine::new(&args.index)?;
    info!("✅ Search engine initialized successfully");

    // Create shared state
    let app_state = server::AppState {
        database,
        search_engine,
        config,
    };

    // Create routes
    let routes = create_routes(app_state);

    // Add CORS headers
    let cors = warp::cors()
        .allow_any_origin()
        .allow_headers(vec!["content-type"])
        .allow_methods(vec!["GET", "POST", "PUT", "DELETE", "OPTIONS"]);

    let routes = routes.with(cors);

    // Parse socket address
    let addr: SocketAddr = format!("{}:{}", args.host, args.port).parse()?;

    info!("🚀 Starting knowledge server...");
    info!("📡 API endpoint: http://{}", addr);
    info!("❤️ Health check: http://{}/health", addr);
    info!("📖 Search endpoint: http://{}/api/search", addr);
    info!("📝 Knowledge endpoint: http://{}/api/knowledge", addr);
    info!("");
    info!("Press Ctrl+C to stop the server.");

    // Start the server
    warp::serve(routes)
        .run(addr)
        .await;

    info!("👋 Knowledge server shutting down gracefully");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_args_parsing() {
        let args = Args::parse_from(&["knowledge-server", "--host", "0.0.0.0", "--port", "9000"]);
        assert_eq!(args.host, "0.0.0.0");
        assert_eq!(args.port, 9000);
    }
}