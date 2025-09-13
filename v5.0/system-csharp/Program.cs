using SaraAI.SystemControl.Services;
using Serilog;

namespace SaraAI.SystemControl;

/// <summary>
/// Main entry point for the SaraAI System Control module
/// </summary>
public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("⚙️ Starting SaraAI System Control Module");
        Console.WriteLine("==========================================");

        // Configure Serilog
        Log.Logger = new LoggerConfiguration()
            .MinimumLevel.Information()
            .WriteTo.Console(outputTemplate: 
                "{Timestamp:yyyy-MM-dd HH:mm:ss} [{Level:u3}] {Message:lj}{NewLine}{Exception}")
            .WriteTo.File("logs/system-control-.log", 
                rollingInterval: RollingInterval.Day,
                retainedFileCountLimit: 7)
            .CreateLogger();

        try
        {
            Log.Information("🚀 Initializing System Control module...");

            var builder = WebApplication.CreateBuilder(args);

            // Use Serilog for logging
            builder.Host.UseSerilog();

            // Configure services
            ConfigureServices(builder.Services, builder.Configuration);

            var app = builder.Build();

            // Configure the HTTP request pipeline
            ConfigurePipeline(app);

            // Display startup information
            var port = builder.Configuration["urls"] ?? "http://localhost:8003";
            Log.Information("✨ System Control module is running!");
            Log.Information("📡 API endpoint: {Endpoint}", port);
            Log.Information("📋 Swagger UI: {SwaggerUrl}/swagger", port);
            Log.Information("❤️ Health check: {HealthUrl}/health", port);

            // Run the application
            app.Run();
        }
        catch (Exception ex)
        {
            Log.Fatal(ex, "❌ System Control module failed to start");
        }
        finally
        {
            Log.CloseAndFlush();
        }
    }

    /// <summary>
    /// Configure dependency injection services
    /// </summary>
    private static void ConfigureServices(IServiceCollection services, IConfiguration configuration)
    {
        // Add controllers
        services.AddControllers();

        // Add API documentation
        services.AddEndpointsApiExplorer();
        services.AddSwaggerGen(c =>
        {
            c.SwaggerDoc("v1", new Microsoft.OpenApi.Models.OpenApiInfo
            {
                Title = "SaraAI System Control API",
                Version = "v1",
                Description = "System integration and control API for SaraAI",
                Contact = new Microsoft.OpenApi.Models.OpenApiContact
                {
                    Name = "SaraAI Team"
                }
            });
        });

        // Add HTTP client for inter-module communication
        services.AddHttpClient();

        // Add custom services
        services.AddScoped<ISystemService, SystemService>();
        services.AddScoped<IFileSystemService, FileSystemService>();
        services.AddScoped<IProcessService, ProcessService>();

        // Configure CORS
        services.AddCors(options =>
        {
            options.AddDefaultPolicy(builder =>
            {
                builder.AllowAnyOrigin()
                       .AllowAnyMethod()
                       .AllowAnyHeader();
            });
        });

        // Add health checks
        services.AddHealthChecks();

        Log.Information("✅ Services configured successfully");
    }

    /// <summary>
    /// Configure the HTTP request pipeline
    /// </summary>
    private static void ConfigurePipeline(WebApplication app)
    {
        // Development-specific middleware
        if (app.Environment.IsDevelopment())
        {
            app.UseSwagger();
            app.UseSwaggerUI(c =>
            {
                c.SwaggerEndpoint("/swagger/v1/swagger.json", "SaraAI System Control API v1");
                c.RoutePrefix = "swagger";
            });
        }

        // Enable CORS
        app.UseCors();

        // Add routing
        app.UseRouting();

        // Map controllers
        app.MapControllers();

        // Map health check endpoint
        app.MapHealthChecks("/health");

        // Add a simple root endpoint
        app.MapGet("/", () => new
        {
            service = "SaraAI System Control",
            version = "1.0.0",
            status = "running",
            timestamp = DateTime.UtcNow,
            endpoints = new
            {
                health = "/health",
                swagger = "/swagger",
                system = "/api/system",
                files = "/api/files",
                processes = "/api/processes"
            }
        });

        Log.Information("✅ HTTP pipeline configured successfully");
    }
}