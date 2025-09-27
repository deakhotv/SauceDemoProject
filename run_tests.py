#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil

def run_command(command, description):
    """Run a shell command and print output"""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {command}")
    return result.returncode

def cleanup_directories():
    """Clean up generated directories"""
    directories = ['allure-results', 'allure-report', '__pycache__', '.pytest_cache']
    for dir_name in directories:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🧹 Cleaned up: {dir_name}")

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    return run_command("pip install -r requirements.txt", "Installing dependencies")

def run_individual_tests():
    """Run tests individually"""
    print("\n🔍 Running Individual Tests")
    
    run_command(
        "pytest tests/test_q1_locked_user.py -v -m q1 --alluredir=allure-results", 
        "Q1 - Locked User Test"
    )
    
    run_command(
        "pytest tests/test_q2_standard_user.py -v -m q2 --alluredir=allure-results", 
        "Q2 - Standard User Test"
    )
    
    run_command(
        "pytest tests/test_q3_performance_user.py -v -m q3 --alluredir=allure-results", 
        "Q3 - Performance User Test"
    )

def run_all_tests_sequentially():
    """Run all tests sequentially"""
    print("\n🎯 Running All Tests Sequentially")
    return run_command(
        "pytest tests/ -v --alluredir=allure-results", 
        "All Tests Sequential Run"
    )

def generate_allure_report():
    """Generate Allure report"""
    print("\n📊 Generating Allure Report")
    
    result = run_command(
        "allure generate allure-results --clean -o allure-report", 
        "Generating Allure HTML Report"
    )
    
    if result == 0:
        report_path = os.path.abspath("allure-report/index.html")
        print(f"✅ Allure report generated: file://{report_path}")
        
        try:
            if sys.platform == "win32":
                os.startfile(report_path)
            elif sys.platform == "darwin":
                subprocess.run(["open", report_path])
            else:
                subprocess.run(["xdg-open", report_path])
        except:
            print("ℹ️  Report generated but could not open automatically")
    
    return result

def main():
    """Main execution function"""
    print("🎪 SauceDemo Automation Test Suite")
    print("📋 Running all three test scenarios as required")
    
    cleanup_directories()
    
    if install_dependencies() != 0:
        print("❌ Failed to install dependencies")
        return 1
    
    os.makedirs("allure-results", exist_ok=True)
    
    run_individual_tests()
    run_all_tests_sequentially()
    
    generate_allure_report()
    
    print("\n" + "="*60)
    print("✅ Test Execution Completed Successfully!")
    print("="*60)
    print("\n📁 Generated Files:")
    print("   - allure-results/    : Test execution results")
    print("   - allure-report/     : HTML report (open index.html in browser)")
    print("\n🎯 To run tests again, use: python run_tests.py")
    print("📊 To view report: allure serve allure-results")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())