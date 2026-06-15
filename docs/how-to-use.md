# How to Use This Repository

## For CMMC Compliance Implementation in Azure

1. **Identify your CMMC level** — Level 1 (FCI only) or Level 2 (CUI handling).
2. **Navigate to the appropriate mappings folder**:
   - `mappings/level1/` for CMMC Level 1 (17 practices)
   - `mappings/level2/` for CMMC Level 2 (110 practices)
3. **Open the domain file** relevant to the control you want to implement (e.g., `AC-access-control.md` for Access Control).
4. **Follow the Azure implementation guidance** for each practice, including:
   - Which Azure service satisfies the control
   - Which AZ-104 skill area the implementation falls under
   - Configuration steps and notes

## For AZ-104 Exam Preparation with CMMC Context

1. **Open the CSV files** in the `/csv/` folder.
2. **Filter by AZ-104 Exam Domain** to see which CMMC controls relate to each exam section.
3. **Study the Azure service** listed and understand how it fulfills the compliance control — this reinforces both exam prep and real-world knowledge.

## Reading the Mapping Tables

Each mapping entry contains:

| Column | Description |
|--------|-------------|
| **Practice ID** | CMMC practice identifier (e.g., `AC.L1-3.1.1`) |
| **Practice Name** | Short name of the CMMC practice |
| **Control Description** | What the control requires |
| **AZ-104 Domain** | The AZ-104 exam domain this maps to |
| **AZ-104 Skill** | The specific AZ-104 skill or sub-skill |
| **Azure Service(s)** | Azure service(s) used to implement the control |
| **Implementation Notes** | Guidance on how to configure/use the service |
| **NIST 800-171 Ref** | Underlying NIST SP 800-171 requirement (Level 2) |

## CSV Usage

The CSV files can be opened in:
- **Microsoft Excel** — Use filters on the AZ-104 Domain or CMMC Domain column
- **Google Sheets** — Import via File > Import
- **Python/pandas** — `pd.read_csv('cmmc-level1-az104-mapping.csv')`
- **Any text editor** — Raw comma-separated values

## Scope Notes

- **Physical Protection (PE)** controls are mostly satisfied through Azure's data center physical security (covered under the Microsoft Shared Responsibility Model). Some PE controls require customer-side documentation.
- **Personnel Security (PS)** and **Awareness and Training (AT)** controls require organizational policies that Azure services support but do not fully automate.
- Controls marked `[Partial]` in the implementation notes require both Azure configuration AND documented organizational policy.
