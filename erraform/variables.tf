variable "gcp_project_id" {
  type        = string
  description = "The ID of the Google Cloud Project for The Seven Worlds"
  default     = "the-seven-worlds-gemini"
}

variable "gcp_region" {
  type        = string
  description = "The primary cloud region for Gemini Bird AI deployment"
  default     = "us-central1"
}

variable "storage_bucket_name" {
  type        = string
  description = "The unique name for the infinite storage bucket"
  default     = "gemini-bird-infinite-storage-bucket"
}

