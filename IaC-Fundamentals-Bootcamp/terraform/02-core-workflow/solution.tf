# Solution - write your work here
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.9.0"
    }
  }
}

provider "azurerm" {
  features {}
}

provider "local" {}

resource "local_file" "terraformrocks" {
  filename = "terraformrocks.txt"
  content  = "Terraform rocks!"
}