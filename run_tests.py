#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil
import argparse

def print_header(text):
    """Print formatted header"""
    print(f"\n{'='*70}")
    print(f"🚀 {text}")
    print(f"{'='*70}")

def run_command(command, description, check=True):
    """Run a shell command and print output"""
    print_header(description)
    print(f"Command: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=check)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with exit code {e.returncode}")
        if check:
            raise
        return e.returncode

def cleanup_directories():
    """Clean up generated directories"""
    directories = ['allure-results', 'allure-report', '__pycache__', '.pytest_cache', 'html-report']
    for dir_name in directories:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🧹 Cleaned up: {dir_name}")

def install_dependencies():
    """Install required dependencies"""
    return run_command("pip install -r requirements.txt", "Installing dependencies")

def run_tests_with_options(browser="chrome", headless=True, markers=None):
    """Run tests with specific options"""
    cmd = "pytest tests/ -v"
    
    if browser:
        cmd += f" --browser {browser}"
    if headless:
        cmd += " --headless"
    if markers:
        cmd += f" -m {markers}"
    
    cmd += " --alluredir=allure-results"
    
    return run_command(cmd, "Running Tests")

def run_individual_tests():
    """Run tests individually"""
    tests = [
        ("Q1 - Locked User Test", "tests/test_q1_locked_user.py"),
        ("Q2 - Standard User Test", "tests/test_q2_standard_user.py"),
        ("Q3 - Performance User Test", "tests/test_q3_performance_user.py")
    ]
    
    for test_name, test_path in tests:
        cmd = f"pytest {test_path} -v --alluredir=allure-results"
        run_command(cmd, test_name, check=False)

def generate_allure_report():
    """Generate Allure report"""
    # Check if allure is available
    try:
        subprocess.run(["allure", "--version"], check=True, capture_output=True)
    except:
        print("❌ Allure commandline not found. Installing...")
        # Try to install allure
        run_command("pip install allure-pytest", "Installing allure-pytest", check=False)
    
    result = run_command(
        "allure generate allure-results --clean -o allure-report", 
        "Generating Allure HTML Report",
        check=False
    )
    
    if result == 0:
        report_path = os.path.abspath("allure-report/index.html")
        print(f"✅ Allure report generated: file://{report_path}")
        
        # Offer to open the report
        try:
            open_report = input("\n📊 Would you like to open the Allure report? (y/n): ").lower()
            if open_report in ['y', 'yes']:
                if sys.platform == "win32":
                    os.startfile(report_path)
                elif sys.platform == "darwin":
                    subprocess.run(["open", report_path])
                else:
                    subprocess.run(["xdg-open", report_path])
        except:
            print("ℹ️  Report generated but could not open automatically")
    
    return result
